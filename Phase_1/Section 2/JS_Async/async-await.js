// async function fname() { // Will create a promise
//   console.log('Hello')
//   return 'Ray Wienand' // Promise
// }

// let a = fname()
// console.log(a)

const axios = require('axios')

const github_api = "https://api.github.com/users/"

// const userName = 'keenwarrior'
const userName = 'ray-wienand'

const promise = axios.get(github_api + userName)

async function fetchOrgs(userName) {
  console.log('This will happen first')
  let response = await axios.get(github_api + userName) // Force us to wait for a response
  let orgsResponse = await axios.get(response.data.organizations_url) // This is a list
  let orgs = []
  for (let org of orgsResponse.data) {
    orgs.push(org.login)
  }
  return orgs
}

let out = fetchOrgs(userName) // It calls for this
console.log(out)
out.then((orgs) => {
  console.log(orgs)
})

console.log('Then this will happen')

console.log('Now the response will happen')