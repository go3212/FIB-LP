myMap :: (a -> b) -> [a] -> [b]
myMap f a = [f x | x <- a]

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f xs = [x | x <- xs, f x]

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f xs ys = [f (fst x) (snd x) | x <- zip xs ys]

thingify :: [Int] -> [Int] -> [(Int, Int)]
thingify xs ys = [(x, y) | x <- xs, y <- ys, x `mod` y == 0]

factors :: Int -> [Int]
factors x = [k | k <- [1..x], x `mod` k == 0]