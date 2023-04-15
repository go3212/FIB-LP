data Queue a = Queue [a] [a] deriving (Show)

create :: Queue a
create = Queue [] []

push :: a -> Queue a -> Queue a
push x (Queue fl sl) = Queue fl (x:sl)

pop :: Queue a -> Queue a
pop (Queue [] sl) = pop (Queue (reverse sl) [])
pop (Queue fl sl) = Queue (drop 1 fl) sl

top :: Queue a -> a
top (Queue [] sl) = top (Queue (reverse sl) [])
top (Queue fl sl) = head fl

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty _ = False

instance Eq a => Eq (Queue a)
    where 
    q1 == q2 = toList q1 == toList q2
        where
            toList (Queue front back) = front ++ reverse back

instance Functor Queue where
    fmap f (Queue front back) = Queue (map f front) (map f back)

translation :: Num b => b -> Queue b -> Queue b
translation n q = fmap (\x -> x + n) q

instance Applicative Queue where
    pure x = Queue [x] []
    (Queue ffront fback) <*> (Queue xfront xback) = Queue (ffront <*> xfront) (fback <*> xback)

instance Monad Queue where
    return = pure
    (Queue front back) >>= f = concatQueues $ fmap f (Queue front back)
        where
            concatQueues (Queue front back) = foldr appendQueue (Queue [] []) (front ++ reverse back)
            appendQueue (Queue xfront xback) (Queue front back) = Queue (xfront ++ front) (xback ++ back)

kfilter :: (p -> Bool) -> Queue p -> Queue p
kfilter predicate queue = do
    x <- queue
    if predicate x
        then return x
        else emptyQueue
  where
    emptyQueue = Queue [] []



