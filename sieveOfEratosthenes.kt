fun main(args: Array<String>) {
	val upTo =  if  (args.size > 0)  args[0].toInt()  else 0
    val nums = Array((upTo/2 -1), {i -> (i+1)*2 + 1})
	val isPrime = nums.associate{it to true}.toMutableMap()
	for ( stepBy in nums) {
		if ( isPrime.get(stepBy)!! ){
			for (n in stepBy*2..upTo+stepBy step stepBy) {
				isPrime.set(n, false)
			}
		}	
	}
	
	val primes = listOf(2) + nums.filter( {it -> isPrime.get(it) == true} )
	println(primes)
	print("There are " + primes.size +" primes up to " + (upTo))
}