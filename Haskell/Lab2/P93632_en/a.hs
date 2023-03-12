eql :: [Int] -> [Int] -> Bool
eql xs ys 
    | length xs /= length ys = False
    | otherwise = and (zipWith (==) xs ys)

prod :: [Int] -> Int
prod xs = foldl (\x y -> x*y) 1 xs

prodOfEvens :: [Int] -> Int
prodOfEvens xs = prod [x | x <- xs, x `mod` 2 == 0]

powersOf2 :: [Int]
powersOf2 = [2^n | n <- [0..]]

scalarProduct :: [Float] -> [Float] -> Float
scalarProduct xs ys = foldl (+) 0 $ zipWith (*) xs ys