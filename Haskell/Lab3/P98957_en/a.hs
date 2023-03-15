import Data.List

ones :: [Integer]
ones = [1 | x <- [1..]]

nats :: [Integer] 
nats = [x | x <- [0..]]

ints :: [Integer]
ints = [0] ++ concat [[n, -n]| n <- [1..]]

triangulars :: [Integer]
triangulars = [sum [0..n] | n <- [0..]]

factorials :: [Integer]
factorials = [foldl (*) 1 [1..n] | n <- [0..]]

fibs :: [Integer]
fibs = [fst x | x <- iterate (\(a,b) -> (b,a+b)) (0,1)]

primes :: [Integer]
primes = [x | x <- [2..], isPrime x]
    where 
        isPrime :: Integer -> Bool -- Un numero es primo si solo lo divide 1 y el mismo.
        isPrime 0 = False
        isPrime 1 = False
        isPrime x = (not $ any (\x -> True) [k | k <- [2..((floor . sqrt . fromIntegral) x)], x `mod` k == 0])

hammings :: [Integer]
hammings = 1 : mergeUnique (map (2*) hammings) (mergeUnique (map (3*) hammings) (map (5*) hammings))
    where 
        mergeUnique :: [Integer] -> [Integer] -> [Integer]
        mergeUnique xs ys = (unique $ merge xs ys)
        
        unique :: [Integer] -> [Integer]
        unique [] = []
        unique (x:xs)  = x : (unique $ dropWhile (==x) xs)

        merge :: [Integer] -> [Integer] -> [Integer]
        merge [] [] = []
        merge [] ys = ys
        merge xs [] = xs
        merge (x:xs) (y:ys) 
            |  x < y = x : (merge xs (y:ys))
            |  x > y = y : (merge (x:xs) ys)
            |  otherwise = x : y : (merge xs ys)

-- Funcion ineficiente
-- hammings = [x | x <- [1..], (length . filter (>5) . factors) x == 0 ]
--     where
--         factors :: Integer -> [Integer]
--         factors x = rf x (takeWhile (<=x) primes)
--             where 
--                 rf :: Integer -> [Integer] -> [Integer]
--                 rf _ [] = []
--                 rf k (x:xs)
--                     | k < 2 = []
--                     | k < x^2  = [k]
--                     | k `mod` x == 0 = x : rf (k `div` x) ([x] ++ xs)
--                     | otherwise = rf k xs 

lookNsay :: [Integer]
lookNsay = [1] ++ gLookNSay 1

gLookNSay :: Integer -> [Integer]
gLookNSay x = [next] ++ gLookNSay next 
    where 
        next :: Integer
        next = foldl (\x y -> (10^(integerLength $ digits $ y))*x + y) (0) $ map (\ks -> (integerLength ks)*10 +  head ks) $ packSeq x
        integerLength :: [Integer] -> Integer
        integerLength [] = 0
        integerLength (x:xs) = 1 + integerLength xs
        constr :: [Integer] -> Integer
        constr xs = foldl (\x y -> x*10 + y) 0 xs
        digits :: Integer -> [Integer]
        digits = map (read . (:[])) . show
        packSeq :: Integer -> [[Integer]]
        packSeq x
            | length nextDecon == 0 = [newDecon]
            | otherwise = [newDecon] ++ (packSeq $ constr $ nextDecon)
            where 
                newDecon =  takeWhile (== head decons) decons
                nextDecon = dropWhile (== head decons) decons
                decons = digits x

tartaglia :: [[Integer]]
tartaglia = [[binCoef x k | k <- [0..x]] | x <- [0..]]
    where 
        binCoef :: Integer -> Integer -> Integer
        binCoef u d = (fact u) `div` ((fact d)*(fact (u+(-d))))
        fact :: Integer -> Integer
        fact 0 = 1
        fact 1 = 1
        fact x = x*(fact (x + (-1)))