data STree a = Nil | Node Int a (STree a) (STree a) deriving Show

isOk :: STree a -> Bool
isOk Nil = True
isOk (Node size _ left right) =
  size == 1 + getSize left + getSize right &&
  isOk left &&
  isOk right
  where
    getSize Nil = 0
    getSize (Node size _ _ _) = size

nthElement :: STree a -> Int -> Maybe a
nthElement Nil _ = Nothing
nthElement (Node size value left right) n
  | n <= 0 || n > size = Nothing
  | n <= getSize left = nthElement left n
  | n == getSize left + 1 = Just value
  | otherwise = nthElement right (n - getSize left - 1)
  where
    getSize Nil = 0
    getSize (Node size _ _ _ ) = size

mapToElements :: (a -> b) -> STree a -> [Int] -> [Maybe b]
mapToElements f tree = map (monadElement f . nthElement tree)
  where
    monadElement :: (a -> b) -> Maybe a -> Maybe b
    monadElement f Nothing = Nothing
    monadElement f (Just a) = Just (f a)

-- Hacer que STree sea functor
instance Functor STree where
    fmap f Nil = Nil
    fmap f (Node size val left right) = Node size (f val) (fmap f left) (fmap f right)
