Funciones de haskell interesantes...
filter
sum
foldr
foldl
read
words
sum
getContents
map

Functor:
Un functor es un tipo de dato en Haskell que se puede mapear mediante la aplicación de una función a sus elementos. Es decir, los funtores son tipos de datos que admiten una operación de "mapeo" o "transformación" sobre sus valores.

class Functor f where
  fmap :: (a -> b) -> f a -> f b

Applicative:
En Haskell, Applicative es una clase de tipos que se utiliza para representar valores que pueden ser aplicados a una función. La clase Applicative extiende la clase Functor, lo que significa que todos los tipos de datos que son instancias de la clase Applicative también son instancias de la clase Functor.

class Functor f => Applicative f where
  pure  :: a -> f a
  (<*>) :: f (a -> b) -> f a -> f b

Monad:
En Haskell, un Monad es un tipo de dato que representa una secuencia de computaciones. Los Monads se utilizan para encapsular cálculos complejos y permiten manipular la secuencia de cálculos de una manera flexible y componible.

class Applicative m => Monad m where
  return :: a -> m a
  (>>=) :: m a -> (a -> m b) -> m b

