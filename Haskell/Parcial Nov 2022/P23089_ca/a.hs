myUnfoldr :: (b -> Maybe (a, b)) -> b -> [a]
myUnfoldr f x = 
    case f x of
        Nothing -> []
        Just (a, b) -> a : myUnfoldr f b     


myReplicate :: a -> Int -> [a]
myReplicate x n = take n $ myUnfoldr (\x -> Just (x, x)) x