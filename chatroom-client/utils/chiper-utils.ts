import CryptoJS from "crypto-js";

var ciphertext = CryptoJS.AES.encrypt('Helllo World', '3d4b7b09924e406ba946cab489b08bd2').toString();
ciphertext
var bytes  = CryptoJS.AES.decrypt(ciphertext, '3d4b7b09924e406ba946cab489b08bd2');
var originalText = bytes.toString(CryptoJS.enc.Utf8);
originalText