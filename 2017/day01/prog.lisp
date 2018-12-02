(defun load-file (filename)
  (with-open-file (in filename)
    (with-standard-io-syntax
      (setf *db* (read in)))))

(defun to-string ()
  (write-to-string *db*))



