const express = require('express')
const app = express()
const port = 8000

app.get('/item', (req, res) => res.send({'version': 0, 'service': 'node'}))

app.listen(port, () => console.log(`Express app started on port ${port}`))