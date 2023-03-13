import Data.List

ones :: [Integer]
ones = [1 | x <- [1..]]

nats :: [Integer] 
nats = [x | x <- [0..]]

ints :: [Integer]
ints = [0] ++ concat [[n, -n]| n <- [1..]]

triangulars :: [Integer]
triangulars = [sum [1..n] | n <- [1..]]

factorials :: [Integer]
factorials = [foldl (*) 1 [1..n] | n <- [0..]]

fibs :: [Integer]
fibs = [fst x | x <- iterate (\(a,b) -> (b,a+b)) (0,1)]

primes :: [Integer]
primes = [x | x <- [2..], isPrime x]
    where 
        isPrime :: Integer -> Bool -- Un numero es primo si solo lo divide 1 y el mismo.
        isPrime x = length [k | k <- [1..x], x `mod` k == 0] == 2

hammings :: [Integer]
hammings = [(2^x)*(3^y)*(5^z) | x <- [0..], y <- [0..], z <- [0..]]