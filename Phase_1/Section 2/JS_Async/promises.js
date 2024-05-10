
// This does not clear out the 1st setTimeout. It runs indefinitely
// const promise = new Promise((resolve, reject) => {
//   setTimeout(() => {
//     resolve('Success')
//   }, 2000);

//   // This will complete first and give failure
//   setTimeout(() => {
//     reject('Failure');
//   }, 1000)
// });

// Catch the message of the promise
// promise.then((message) => {
//   console.log(message)
// }).catch((message) => {
//   console.log(message)
// })

// // Better way. It clears out the unused setTimeout
// const promise = new Promise((resolve, reject) => {
//   const t1 = setTimeout(() => {
//     resolve('Success')
//   }, 2000);

//   // This will complete first and give failure
//   // If the 2nd time is longer than the 1st time it will wait for the 2nd time to run out before console.log
//   const t2 = setTimeout(() => {
//     reject('Failure');
//   }, 1000)
// });

// // Catch the message of the promise
// promise.then((message) => {
//   console.log(message)
// }).catch((message) => {
//   console.log(message)
// })

// Better way. It clears out the unused setTimeout
const promise = new Promise((resolve, reject) => {
  const t1 = setTimeout(() => {
    resolve('Success')
  }, 2000);

  // This will complete first and give failure
  // If the 2nd time is longer than the 1st time it will wait for the 2nd time to run out before console.log
  const t2 = setTimeout(() => {
    reject('Failure');
  }, 1000)
});

// Catch the message of the promise
promise.then((message) => {
  console.log(message)
}).catch((message) => {
  console.log(message)
})