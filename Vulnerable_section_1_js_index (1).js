 const app = express();
 // const path = require('path');
 console.log('start index');
const http = require('http');
 const https = require('https');
 const fs = require('fs');
 require('dotenv').config();
 const httpsServer = https.createServer(httpsOptions, app);
 
 // Redirect HTTP to HTTPS
const httpServer = http.createServer((req, res) => {
  res.writeHead(301, { Location: `https://${req.headers.host}${req.url}` });
  res.end();
});
 
 // Start HTTPS and HTTP servers
 // const HTTPS_PORT = 443;
 // const HTTP_PORT = 80;
 const HTTPS_PORT = 3443;
const HTTP_PORT = 3005;
 // const HTTPS_PORT = process.env.HTTPS_PORT || 3443;
 // const HTTP_PORT = process.env.HTTP_PORT || 3005;
 const HOST =process.env.HOST || "127.0.0.1"
   console.log(`https://${HOST}:${HTTPS_PORT}`);
 });
 
httpServer.listen(HTTP_PORT, () => {
  console.log(`HTTP server listening on port ${HTTP_PORT}`);
  console.log(`http://${HOST}:${HTTP_PORT}`);
 
});