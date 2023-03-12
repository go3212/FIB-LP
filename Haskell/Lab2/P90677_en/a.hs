myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl fs a [] = a
myFoldl fs a (x:xs) = myFoldl fs (fs a x) xs

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr fs a [] = a
myFoldr fs a (x:xs) = fs x (myFoldr fs a xs)

myIterate :: (a -> a) -> a -> [a]
myIterate fs a = [a] ++ myIterate fs (fs a)

myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil fb fs a 
    | fb a = a
    | otherwise = myUntil fb fs (fs a)

myMap :: (a -> b) -> [a] -> [b]
myMap f a = myFoldr (\x y -> f x : y) [] a

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter fb xs = [x | x <- xs, fb x]

myAll :: (a -> Bool) -> [a] -> Bool
myAll fb [] = True
myAll fb xs = and $ map (\x-> fb x) xs

myAny :: (a -> Bool) -> [a] -> Bool
myAny fb [] = False
myAny fb xs = or $ map (\x-> fb x) xs

myZip :: [a] -> [b] -> [(a, b)]
myZip [] [] = []
myZip [] ys = []
myZip xs [] = []
myZip (x:xs) (y:ys) = [(x, y)] ++ myZip xs ys

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f xs ys = map (\x -> f (fst x) (snd x)) $ myZip xs ys


