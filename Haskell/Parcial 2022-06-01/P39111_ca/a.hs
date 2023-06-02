import Data.List (sort)

type Pos  = (Int, Int)

dins :: Pos -> Bool
dins (x, y) = x <= 8 && x >= 1 && y <= 8 && y >= 1

moviments :: Pos -> [Pos]
moviments  (x, y) = sort $ filter dins 
    [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1),(x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]

potAnar3 :: Pos -> Pos -> Bool
potAnar3 p q = q `elem` saltos3
  where
    saltos1 = moviments p
    saltos2 = concatMap moviments saltos1
    saltos3 = concatMap moviments saltos2

potAnar3' :: Pos -> Pos -> Bool
potAnar3' p q = do
    let primerSalto = moviments p
    let segundoSalto = concatMap moviments primerSalto
    let tercerSalto = concatMap moviments segundoSalto
    q `elem` tercerSalto


                       
