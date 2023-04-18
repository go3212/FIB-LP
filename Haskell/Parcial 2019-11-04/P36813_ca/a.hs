import Data.List

-- El grado de un vértice son todas las aristas que indicen en el ...
degree :: Eq a => [(a, a)] -> a -> Int
degree [] v = 0
degree (e:es) v 
    | fst e == v || snd e == v = 1 + degree es v
    | otherwise = degree es v
    
degree' :: Eq a => [(a, a)] -> a -> Int 
degree' e v = length $ filter (\(v1, v2) -> v == v1 || v == v2) e

-- Los vecinos de un vértice son aquellos que se encuentrar en una tupla...
neighbors :: Ord a => [(a, a)] -> a -> [a]
neighbors e v = sort $ map (getNeighbor v) $ filter (\(v1, v2) -> v == v1 || v == v2) e
    where 
        getNeighbor :: Ord a => a -> (a, a) -> a
        getNeighbor v (v1 ,v2)
            | v1 == v = v2
            | otherwise = v1