absValue :: Int -> Int
absValue x 
    | x < 0 = (-1)*x
    | otherwise = x

power :: Int -> Int -> Int
power x 0 = 1
power x p = x*(power x (p-1))

isPrime :: Int -> Bool -- Un numero es primo si solo lo divide 1 y el mismo.
isPrime x = length [k | k <- [1..x], x `mod` k == 0] == 2

slowFib :: Int -> Int
slowFib 0 = 0
slowFib 1 = 1
slowFib x = slowFib (x+(-1)) + slowFib (x+(-2))


quickFib :: Int -> Int
quickFib n = go n (0, 1)
  where
    go 0 (a, _) = a
    go n (a, b) = go (n-1) (b, a+b)
