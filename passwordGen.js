// const passwordGenerator = (passwordNeededLength=12) => {
//     const characters = ['a','b','c','d','e','f','g','!' ,'@','$','%','k','l', 'm', 'n','o','p','2','4','6','7','8','9', 'Q', 'R', 'S','T','U','V','W','X','Y', 'Z']
//     let string = ''
//     let length = passwordNeededLength
//     let count = 0 
//     while (count < length){
//         let randomChar = Math.floor(Math.random() * characters.length)
//         string = string + characters[randomChar]
//         count ++ 
//     }
//     return string
// }

// console.log(passwordGenerator())

const passwordGenerator = (length=12) => {
    let string = ''
    const characters = ['a','b','c','d','e','f','g','!' ,'@','$','%','k','l', 'm', 'n','o','p','2','4','6','7','8','9', 'Q', 'R', 'S','T','U','V','W','X','Y', 'Z']
    let count = 0 
    while (count < length){
        let randomChar = Math.floor(Math.random() * characters.length)
        string = string + characters[randomChar]
        count ++ 
    }
    return string
}



console.log(passwordGenerator())







