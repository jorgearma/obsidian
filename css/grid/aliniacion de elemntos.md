
```css
.contenedor {
	display: grid;
	grid-gap: 20px;
	grid-template-columns: repeat(3, 1fr);
	grid-template-rows: repeat(3, 200px);

	/* Alinea Horizontalmente */
	justify-items: center;
	/* auto \ start \ center \ end \ stretch */

	/* Alinea Verticalmente */
	align-items: center;
	/* auto \ start \ center \ end \ stretch */
}

.contenedor .item {
	background: #ff8000;
	justify-self: stretch;
	align-self: stretch;
}
```