import Text.Printf (printf)

getResponse :: String -> String
getResponse ('A':_) = "Hello!"
getResponse ('a':_) = "Hello!"
getResponse _ = "Bye!"

main :: IO ()
main = do
    input <- getContents
    printf "%s\n" (getResponse input)