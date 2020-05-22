(defvar a )
(defvar n)
(princ "Enter list: ")

(setq a (read-from-string (concatenate 'string "(" (read-line) ")")))

(princ "List is: ")
(princ a)
(terpri)

(princ "Enter the index in list: ")

(setq n (read))
(princ "The element is - ")
(princ (nth n  a))

