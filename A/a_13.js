const zlib = require('zlib');

// Base64 encoded strings
const base64Strings = [
  "eJzzyc9Lyc8DAAgpAms=",
  "eJxzSi3KycwDAAfXAl0=",
  "eJzzSy1XiMwvygYADKUC8A=="
];

// Decode and decompress each string
base64Strings.forEach((base64String, index) => {
  const buffer = Buffer.from(base64String, 'base64');

  zlib.unzip(buffer, (err, decompressedBuffer) => {
    if (err) {
      console.error(`Error decoding and decompressing string ${index + 1}: ${err}`);
    } else {
      const city = decompressedBuffer.toString('utf8');
      console.log(`Decoded string ${index + 1}: ${city}`);
    }
  });
});


