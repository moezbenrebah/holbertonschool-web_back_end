const process = require("process");

function displayMessage(arg) {
  process.stdout.write(arg + "\n");
}




module.exports = displayMessage;
