fizzBuzz :: [Either Int String]
fizzBuzz = fizzBuzzRec 0

fizzBuzzRec :: Int -> [Either Int String]
fizzBuzzRec x
    | x `mod` 3 == 0 && x `mod` 5 == 0 = Right "FizzBuzz" : fizzBuzzRec (x+1)
    | x `mod` 3 == 0 = Right "Fizz" : fizzBuzzRec (x+1)
    | x `mod` 5 == 0 = Right "Buzz" : fizzBuzzRec (x+1)
    | otherwise = Left x : fizzBuzzRec (x+1)
