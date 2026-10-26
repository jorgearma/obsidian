# Trusts — confianza entre dominios

> **En una frase:** un **trust** es un acuerdo entre dos dominios para que los usuarios de uno puedan acceder a recursos del otro, es decir, para que **la autenticación cruce la frontera** del dominio. Ojo al detalle que confunde a todos: **la flecha de la confianza apunta al revés que la flecha del acceso.**
> Relacionado: [[kerberos-kdc]] · [[ntlm]] · [[ldap]] · [[agdlp-y-bloodhound]]

---

## El problema que resuelve
Cada dominio es una **frontera** de autenticación: el DC de `nordwind.local` solo conoce a sus usuarios. ¿Y si la empresa compra otra con dominio `baltic.local` y quieres que un usuario de Baltic entre a un share de Nordwind? Sin trust, imposible. El **trust** tiende el puente.

## La analogía — empresa matriz y filial / embajadas
```
NORDWIND (matriz)  ──confía en──►  BALTIC (filial)
```
"Nordwind **confía en** Baltic" = Nordwind **acepta los pases** de Baltic
→ los empleados de **Baltic** pueden entrar a recursos de **Nordwind**.

> 🧭 **La regla de la flecha (clavarla):**
> **La confianza apunta en SENTIDO CONTRARIO al acceso.**
> *A confía en B* ⇒ *los usuarios de B acceden a A.*

## Las dos propiedades que definen un trust
| Propiedad | Opciones | Qué significa |
|---|---|---|
| **Dirección** | Unidireccional / Bidireccional | ¿la confianza va en un sentido o en los dos? |
| **Transitividad** | Transitivo / No transitivo | ¿se extiende a los dominios de más allá, o se queda entre esos dos? |

- **Transitivo:** si A confía en B y B en C, entonces A confía en C (la confianza "fluye").
- **No transitivo:** solo vale entre esos dos, no se propaga.

## Dentro de un bosque vs entre bosques
- **Dentro de un MISMO bosque** (ej. `nordwind.local` y un hijo `eu.nordwind.local`):
  los trusts son **automáticos, bidireccionales y transitivos**. Un bosque es **una sola tela de confianza** → por eso el límite real de seguridad en AD es **el bosque, no el dominio**.
- **Entre bosques distintos:** hay que crear el trust a mano (**forest trust** o **external trust**).

## Cómo funciona por dentro (Kerberos cruzando)
Cuando pides un recurso de un dominio en el que confías, no te dan el TGS directo: el KDC te da un **referral ticket (TGT inter-realm)** cifrado con la **clave del trust** (un secreto compartido entre los dos dominios). Lo presentas al KDC del otro dominio y **ese** te da el TGS final.
```
jan@BALTIC  ──►  KDC Baltic     "quiero \\srv.nordwind.local\share"
            ◄──  referral TGT (cifrado con la clave del TRUST)
            ──►  KDC Nordwind   "toma el referral"
            ◄──  TGS del servicio → accede
```
→ La **clave del trust** es el equivalente a `krbtgt`, pero para cruzar dominios.

## 🔑 Por qué se ataca
1. **La confianza amplía la superficie:** si comprometes un dominio y otro **confía** en él, tienes un pie dentro del otro. Ownear un dominio "pequeño" puede abrir uno "grande".
2. **Escalada hijo → padre (dentro del bosque):** como el bosque es un único límite, desde el dominio hijo se puede escalar al **root del bosque** abusando de **SID history** (inyectar el SID del grupo *Enterprise/Domain Admins* del padre) o forjando **inter-realm/trust tickets**. Es un tema **central de CRTP**.
3. **SID filtering** = la defensa que descarta SIDs "ajenos"; cuando está mal configurado o ausente, el abuso de SID history funciona.

## Dónde encaja en el examen
- **OSCP:** normalmente **un solo dominio** → trusts rara vez caen, pero necesitas el concepto para entender el bosque como límite.
- **CRTP:** **aquí sí, a fondo** → escalada hijo→padre, abuso de trusts entre bosques, SID history. Es de los temas que más te va a dar el sello.

## Lo que DEBO recordar (checklist)
- [ ] Trust = la autenticación **cruza la frontera** del dominio.
- [ ] **La confianza apunta al revés que el acceso:** *A confía en B ⇒ B entra en A.*
- [ ] Dentro del bosque: trusts **automáticos, bidireccionales, transitivos** → el **bosque es el límite de seguridad real**, no el dominio.
- [ ] Entre bosques: hay que crearlos (forest / external).
- [ ] Kerberos cruza con un **referral TGT** cifrado con la **clave del trust**.
- [ ] Ataques: hijo→padre vía **SID history** / trust tickets (tema fuerte de CRTP); **SID filtering** es la defensa.
