;; Auto-generated. Do not edit!


(when (boundp 'serve_connection::Addints)
  (if (not (find-package "SERVE_CONNECTION"))
    (make-package "SERVE_CONNECTION"))
  (shadow 'Addints (find-package "SERVE_CONNECTION")))
(unless (find-package "SERVE_CONNECTION::ADDINTS")
  (make-package "SERVE_CONNECTION::ADDINTS"))
(unless (find-package "SERVE_CONNECTION::ADDINTSREQUEST")
  (make-package "SERVE_CONNECTION::ADDINTSREQUEST"))
(unless (find-package "SERVE_CONNECTION::ADDINTSRESPONSE")
  (make-package "SERVE_CONNECTION::ADDINTSRESPONSE"))

(in-package "ROS")





(defclass serve_connection::AddintsRequest
  :super ros::object
  :slots (_num1 _num2 ))

(defmethod serve_connection::AddintsRequest
  (:init
   (&key
    ((:num1 __num1) 0)
    ((:num2 __num2) 0)
    )
   (send-super :init)
   (setq _num1 (round __num1))
   (setq _num2 (round __num2))
   self)
  (:num1
   (&optional __num1)
   (if __num1 (setq _num1 __num1)) _num1)
  (:num2
   (&optional __num2)
   (if __num2 (setq _num2 __num2)) _num2)
  (:serialization-length
   ()
   (+
    ;; int32 _num1
    4
    ;; int32 _num2
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _num1
       (write-long _num1 s)
     ;; int32 _num2
       (write-long _num2 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _num1
     (setq _num1 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _num2
     (setq _num2 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass serve_connection::AddintsResponse
  :super ros::object
  :slots (_sum ))

(defmethod serve_connection::AddintsResponse
  (:init
   (&key
    ((:sum __sum) 0)
    )
   (send-super :init)
   (setq _sum (round __sum))
   self)
  (:sum
   (&optional __sum)
   (if __sum (setq _sum __sum)) _sum)
  (:serialization-length
   ()
   (+
    ;; int32 _sum
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _sum
       (write-long _sum s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _sum
     (setq _sum (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass serve_connection::Addints
  :super ros::object
  :slots ())

(setf (get serve_connection::Addints :md5sum-) "4781436a0c2affec8025955a6041e481")
(setf (get serve_connection::Addints :datatype-) "serve_connection/Addints")
(setf (get serve_connection::Addints :request) serve_connection::AddintsRequest)
(setf (get serve_connection::Addints :response) serve_connection::AddintsResponse)

(defmethod serve_connection::AddintsRequest
  (:response () (instance serve_connection::AddintsResponse :init)))

(setf (get serve_connection::AddintsRequest :md5sum-) "4781436a0c2affec8025955a6041e481")
(setf (get serve_connection::AddintsRequest :datatype-) "serve_connection/AddintsRequest")
(setf (get serve_connection::AddintsRequest :definition-)
      "int32 num1
int32 num2
---

int32 sum
")

(setf (get serve_connection::AddintsResponse :md5sum-) "4781436a0c2affec8025955a6041e481")
(setf (get serve_connection::AddintsResponse :datatype-) "serve_connection/AddintsResponse")
(setf (get serve_connection::AddintsResponse :definition-)
      "int32 num1
int32 num2
---

int32 sum
")



(provide :serve_connection/Addints "4781436a0c2affec8025955a6041e481")


