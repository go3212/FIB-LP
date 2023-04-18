import Data.List (words)

-- Llegeix una línia d'entrada i la converteix en una llista d'enters
readIntList :: String -> [Int]
readIntList = map read . words

-- Calcula la suma d'una llista d'enters
sumIntList :: [Int] -> Int
sumIntList = sum

-- Converteix un enter en una cadena i el mostra per pantalla
showInt :: Int -> String
showInt = show

-- Programa principal: llegeix la seqüència d'enters de l'entrada estàndard,
-- calcula la suma i la mostra a la sortida estàndard
main :: IO ()
main = do
    input <- getContents
    let intList = readIntList input
    let sum = sumIntList intList
    let sumStr = showInt sum
    putStrLn sumStr
