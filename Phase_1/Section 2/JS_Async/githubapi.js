const axios = require('axios')

const github_api = "https://api.github.com/users/"

const userName = 'ray-wienand'
// const userName = 'keenwarrior'


// const response = axios.get(github_api + userName) // This runs a promise but does not fulfill it
// console.log(response)

// //  This will fulfill the promise
// const promise = axios.get(github_api + userName)
// promise.then((response) => {
//   console.log(response)
// }).catch((error) => {
//   console.log(error)
// })

// //  This will fulfill the promise and log a specific data item
// const promise = axios.get(github_api + userName)
// promise.then((response) => {
//   console.log(response.data.organizations_url)
// }).catch((error) => {
//   console.log(error)
// })

//  To use the url in the data
const promise = axios.get(github_api + userName)

promise.then((response) => {
  const p2 = axios.get(response.data.organizations_url)
  p2.then((response) => {
    console.log(response.data)
  });
}).catch((error) => {
  console.log(error)
})
