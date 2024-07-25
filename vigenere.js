// Fungsi untuk mengonversi karakter menjadi nomor (0 hingga max)
function charToNum(c, base) {
    return base.indexOf(c);
}

// Fungsi untuk mengonversi nomor menjadi karakter
function numToChar(n, base) {
    return base[n];
}

// Fungsi untuk enkripsi teks menggunakan Vigenère Cipher yang mendukung semua karakter
function vigenereEncrypt(plaintext, key, base) {
    const baseLength = base.length;
    const keyRepeated = key.repeat(Math.ceil(plaintext.length / key.length)).slice(0, plaintext.length);
    let ciphertext = '';

    for (let i = 0; i < plaintext.length; i++) {
        let p = plaintext[i];
        let k = keyRepeated[i];
        
        if (base.includes(p)) {
            let pNum = charToNum(p, base);
            let kNum = charToNum(k, base);
            let cNum = (pNum + kNum) % baseLength;
            ciphertext += numToChar(cNum, base);
        } else {
            // Jika karakter tidak ada dalam base, biarkan tetap
            ciphertext += p;
        }
    }

    return ciphertext;
}

// Fungsi untuk dekripsi teks menggunakan Vigenère Cipher yang mendukung semua karakter
function vigenereDecrypt(ciphertext, key, base) {
    const baseLength = base.length;
    const keyRepeated = key.repeat(Math.ceil(ciphertext.length / key.length)).slice(0, ciphertext.length);
    let plaintext = '';

    for (let i = 0; i < ciphertext.length; i++) {
        let c = ciphertext[i];
        let k = keyRepeated[i];
        
        if (base.includes(c)) {
            let cNum = charToNum(c, base);
            let kNum = charToNum(k, base);
            let pNum = (cNum - kNum + baseLength) % baseLength;
            plaintext += numToChar(pNum, base);
        } else {
            // Jika karakter tidak ada dalam base, biarkan tetap
            plaintext += c;
        }
    }

    return plaintext;
}




const base = "<PLaiNI.F7=yCr49`#T?&{oXhVs$xSmJjqROMEk Z!+@c,-}]/UB|1D^nAp2W)lf3[8g5v%(Ywd~G_t>*KzQeu0Hb6";
const plaintext = "The quick brown fox jumps over the lazy dog";
const key = "w09R!";

const encrypted = vigenereEncrypt(plaintext, key, base);
console.log("Encrypted:", encrypted);

const decrypted = vigenereDecrypt(encrypted, key, base);
console.log("Decrypted:", decrypted);
