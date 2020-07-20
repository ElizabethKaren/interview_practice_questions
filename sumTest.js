function threeNumberSum(array, targetSum) {
    array.sort((a,b) => a - b)
      const triplets = []
      let count = 0
      while (count < array.length){
          let cN = array[count]
          let left = array[0]
          let right = array[array.lengh -1]
          let cS = cN + left + right 
          triplets.push(cS)
      }
      console.log(triplets)
  }

