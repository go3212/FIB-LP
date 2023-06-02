-- Definim un tipus per a representar els pius
type Piu = String

-- Funció recursiva que implementa l'algorisme de les Torres de Hanoi
hanoi :: Int -> Piu -> Piu -> Piu -> [(Piu, Piu)]
hanoi 0 _ _ _ = []
hanoi n origen destino auxiliar = hanoi (n-1) origen auxiliar destino ++ [(origen, destino)] ++ hanoi (n-1) auxiliar destino origen

-- Funció principal que llegeix les dades d'entrada, crida a la funció hanoi i mostra la sortida
main :: IO ()
main = do
  -- Llegeix les dades d'entrada
  input <- getLine
  let (n:origen:destino:auxiliar:_) = words input
  let numDiscos = read n :: Int
  
  -- Resol el problema de les Torres de Hanoi
  let solucio = hanoi numDiscos origen destino auxiliar
  
  -- Mostra la solució
  fmap (putStrLn . (\(x, y) -> x ++ " -> " ++ y)) solucio
