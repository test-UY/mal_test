// Malicious POC Application - Node.js
// WARNING: This application uses known vulnerable/malicious dependencies

const express = require('express');
const axios = require('axios');
const lodash = require('lodash');
const minimist = require('minimist');
const eventStream = require('event-stream');
const UAParser = require('ua-parser-js');

const app = express();
const PORT = 3000;

// Parse command line arguments (vulnerable minimist)
const args = minimist(process.argv.slice(2));

// Vulnerable lodash usage
const userInput = { constructor: { prototype: { polluted: true } } };
lodash.merge({}, userInput);

// Vulnerable axios version
app.get('/fetch', async (req, res) => {
  try {
    const url = req.query.url; // Insecure URL handling
    const response = await axios.get(url);
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Using vulnerable ua-parser-js
app.get('/parse-ua', (req, res) => {
  const parser = new UAParser();
  const ua = req.headers['user-agent'];
  const result = parser.setUA(ua).getResult();
  res.json(result);
});

// Vulnerable event-stream usage (potential backdoor)
app.get('/stream', (req, res) => {
  const stream = eventStream.map((data, callback) => {
    callback(null, data);
  });
  res.send('Streaming data...');
});

app.get('/', (req, res) => {
  res.send('Malicious POC Application - DO NOT USE IN PRODUCTION!');
});

app.listen(PORT, () => {
  console.log(`⚠️  WARNING: Malicious POC app running on port ${PORT}`);
  console.log('This application contains known vulnerable dependencies!');
});
