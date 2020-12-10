const express = require('express');
const bodyParser= require('body-parser')
const MongoClient = require('mongodb').MongoClient

const app = express();
app.set('view engine', 'ejs')
// Make sure you place body-parser before your CRUD handlers!
app.use(bodyParser.urlencoded({ extended: true }))
app.use(express.static('public'))
app.use(bodyParser.json())

app.listen(3000, function() {
    console.log('listening on 3000')
  })

// app.get('/', (req, res) => {
//     res.sendFile(__dirname + '/index.html')
//     // Note: __dirname is the current directory you're in. Try logging it and see what you get!
//     // Mine was '/Users/zellwk/Projects/demo-repos/crud-express-mongo' for this app.
// })

// app.post('/quotes', (req, res) => {
//     // console.log(req.body)
//     res.sendFile(__dirname + '/index.html')
//   })

MongoClient.connect('mongodb+srv://test:1234567890@cluster0.plppr.mongodb.net/test?retryWrites=true&w=majority').then(client => {
  // ...
  const db = client.db('star-wars-quotes')
  const quotesCollection = db.collection('quotes')

  app.get('/', (req, res) => {
    db.collection('quotes').find().toArray()
      .then(results => {
        res.render('index.ejs', { quotes: results })
      })
      .catch(error => console.error(error))
  })

  app.post('/quotes', (req, res) => {
    quotesCollection.insertOne(req.body)
      .then(result => {
        // console.log(result)
        res.redirect('/')
      })
      .catch(error => console.error(error))
  })

  app.put('/quotes', (req, res) => {
    // console.log(req.body)
    quotesCollection.findOneAndUpdate(
      { name: req.body.name },
      {
        $set: {
          name: req.body.name,
          quote: req.body.quote
        }
      },
      {
        upsert: true
      }
    )
      .then(result => {res.json('Success')})
      .catch(error => console.error(error))
  })
  
  app.delete('/quotes', (req, res) => {
    quotesCollection.deleteOne(
      { name: req.body.name }
    )
    .then(result => {
      if (result.deletedCount === 0) {
        return res.json('No quote to delete')
      }
      res.json(`Deleted !`)
    })
    .catch(error => console.error(error))
  })
  // app.listen(/* ... */)
}).catch(console.error)
