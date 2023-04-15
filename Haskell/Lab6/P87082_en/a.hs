import Text.Printf (printf)

-- Define a data type to represent a person's information
data Person = Person { name :: String, weight :: Double, height :: Double }

-- Define a function to parse a line of input and convert it into a Person
parseLine :: String -> Person
parseLine line = case words line of
    [name, weightStr, heightStr] -> Person name (read weightStr) (read heightStr)
    _ -> error "Invalid input format"

-- Define a function to calculate a person's BMI
calculateBMI :: Person -> Double
calculateBMI person = weight person / (height person ^ 2)

-- Define a function to categorize a person's BMI
categorizeBMI :: Double -> String
categorizeBMI bmi
    | bmi < 18 = "underweight"
    | bmi <= 25 = "normal weight"
    | bmi <= 30 = "overweight"
    | bmi <= 40 = "obese"
    | otherwise = "severely obese"

-- Define a main function to read input, calculate each person's BMI and category, and print the results
main :: IO ()
main = do
    input <- getContents
    let linesWithoutAsterisk = takeWhile (/= "*") (lines input)
    let people = map parseLine linesWithoutAsterisk
    let bmis = map calculateBMI people
    let categories = map categorizeBMI bmis
    mapM_ (\(person, bmi, category) -> printf "%s: %s\n" (name person) category) (zip3 people bmis categories)
