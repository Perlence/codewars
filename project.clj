(defproject codewars "0.1.0-SNAPSHOT"
  :dependencies [[org.clojure/clojure "1.8.0"]]
  :target-path "target/%s"
  :source-paths ["."]
  :profiles {:uberjar {:aot :all}}
  :plugins [[lein-exec "0.3.6"]])
