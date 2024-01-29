// app.js
const express = require('express');
const bodyParser = require('body-parser');
const fetch = require('node-fetch');
const cheerio = require('cheerio');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.post('/track', async (req, res) => {
  const { trackingNumber } = req.body;
  const trackingURL = `https://parcelsapp.com/en/tracking/${trackingNumber}`;

  // Fetch HTML content of the tracking page
  const response = await fetch(trackingURL);
  const html = await response.text();

  // Parse HTML using Cheerio
  const $ = cheerio.load(html);

  // Extract package status information
  const events = $('.list-unstyled.events .event');

  if (events.length === 0) {
    console.log(`No events found for ${trackingNumber}.`);
  } else {
    // Extracting data from the latest event
    const latestEvent = events.first();
    const eventTime = latestEvent.find('.event-time strong').text();
    const eventDescription = latestEvent.find('.event-content strong').text();
    const eventLocation = latestEvent.find('.event-content .location').text();
    const eventCarrier = latestEvent.find('.event-content .carrier').text();

    // Log the details to the console (you can modify this to send the details to the frontend)
    console.log(`Tracking ${trackingNumber}.`);
    console.log(`Latest event: ${eventDescription} at ${eventLocation} on ${eventTime}. Carrier: ${eventCarrier}`);
  }

  // Send the entire HTML content back to the client
  res.send(html);
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
