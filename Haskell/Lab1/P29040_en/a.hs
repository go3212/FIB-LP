insert :: [Int] -> Int -> [Int]
insert [] x = [x]
insert (y:ys) x
    | x <= y    = x:y:ys 
    | otherwise = y : insert ys x

isort :: [Int] -> [Int]
isort [] = []
isort (x:xs) = insert (isort xs) x

remove :: [Int] -> Int -> [Int]
remove [] k = []
remove (x:xs) k 
    | x == k = xs
    | otherwise = [x] ++ remove xs k

ssort :: [Int] -> [Int]
ssort [] = []
ssort (x:xs)
    | min == x = [x] ++ ssort xs
    | otherwise = [min] ++ (ssort ((remove xs min) ++ [x]))
    where min = minimum $ [x] ++ xs

merge :: [Int] -> [Int] -> [Int]
merge [] [] = []
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys)
    | x < y = [x] ++ merge xs ([y] ++ ys)
    | otherwise = [y] ++ merge ([x] ++ xs) ys

msort :: [Int] -> [Int]
msort [] = []
msort xs 
    | fhl == 0 = sh
    | shl == 0 = fh
    | fhl == 1 && shl == 1 = merge fh sh
    | otherwise = merge (msort fh) (msort sh)
    where 
        (fh, sh) = splitAt ((length xs) `div` 2) xs
        fhl = length fh
        shl = length sh

qsort :: [Int] -> [Int]
qsort [] = []
qsort (x:xs) = fh ++ [x] ++ sh
    where
        fh = qsort [a | a <- xs, a <= x]
        sh = qsort [a | a <- xs, a > x]

genQsort :: Ord a => [a] -> [a]
genQsort [] = []
genQsort (x:xs) = fh ++ [x] ++ sh
    where
        fh = genQsort [a | a <- xs, a <= x]
        sh = genQsort [a | a <- xs, a > x]