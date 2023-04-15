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
