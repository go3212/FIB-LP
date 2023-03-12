countIf :: (Int -> Bool) -> [Int] -> Int
countIf f xs = length (filter f xs)

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam xs fs = map (\f -> map f xs) fs

pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 xs fs = map (\x -> map (\f -> f x) fs) xs

filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int
filterFoldl ft op ac xs = foldl op ac $ filter ft xs

insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert cmp xs x = takeWhile (not . cmp x) xs ++ [x] ++ dropWhile (not . cmp x) xs

insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort cmp [] = []
insertionSort cmp (x:xs) = insert cmp (insertionSort cmp xs) x
