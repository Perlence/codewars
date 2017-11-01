module Codewars.Kata.TenMinuteWalk where

import Debug.Trace
import Test.Hspec
import Control.Exception (evaluate)

isValidWalk :: [Char] -> Bool
isValidWalk walk =
  foldl (\(trail, minutesLeft) direction -> ((processDirection direction trail), minutesLeft - 1)) ([], 10) walk == ([], 0)

processDirection :: Char -> [Char] -> [Char]
processDirection direction [] = [direction]
processDirection direction (lastDirection:trail) =
  if (lastDirection == 'n' && direction == 's') ||
     (lastDirection == 'e' && direction == 'w') ||
     (lastDirection == 's' && direction == 'n') ||
     (lastDirection == 'w' && direction == 'e')
  then
    trail
  else
    direction:lastDirection:trail

main :: IO ()
main = hspec $ do
  describe "Codewars.Kata.TenMinuteWalk.processDirection" $ do
    it "should work" $ do
      processDirection 'n' "" `shouldBe` ("n" :: [Char])
      processDirection 'e' "" `shouldBe` ("e" :: [Char])
      processDirection 'n' "se" `shouldBe` ("e" :: [Char])

  describe "Codewars.Kata.TenMinuteWalk.isValidWalk" $ do
    it "should work" $ do
      isValidWalk "nsnsnsnsns" `shouldBe` (True :: Bool)
      isValidWalk "nsnsnsnsnn" `shouldBe` (False :: Bool)
      isValidWalk "ns" `shouldBe` (False :: Bool)
      isValidWalk "nnnnnsssss" `shouldBe` (True :: Bool)
