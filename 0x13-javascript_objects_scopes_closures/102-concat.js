#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const [, , sourceFileA, sourceFileB, destinationFile] = process.argv;

try {
  const contentA = fs.readFileSync(sourceFileA, 'utf8');
  const contentB = fs.readFileSync(sourceFileB, 'utf8');
  const concatenatedContent = contentA + contentB;

  fs.writeFileSync(destinationFile, concatenatedContent);

  console.log(`Files "${sourceFileA}" and "${sourceFileB}" concatenated successfully to "${destinationFile}".`);
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}