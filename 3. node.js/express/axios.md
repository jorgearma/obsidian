```js
const axios = require('axios');

app.get('/peticion', async (req, res) => {
  try {
    const response = await axios.get('https://jsonplaceholder.typicode.com/posts/1');
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Ocurrió un error al realizar la petición' });
  }
});

```