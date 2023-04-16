divisors :: Int -> [Int] -- Devuelve todos los divisores de el numero
divisors n = [k | k <- [1..n], n `mod` k == 0]

nbDivisors :: Int -> Int
nbDivisors = length . divisors

moltCompost :: Int -> Bool
moltCompost n = foldr (\x y -> x && y) True [nbDivisors k < nDivisors | k <- [1..(n-1)]]
    where 
        nDivisors = nbDivisors n

