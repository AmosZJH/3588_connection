;; Auto-generated. Do not edit!


(when (boundp 'plumbing_test::Servo)
  (if (not (find-package "PLUMBING_TEST"))
    (make-package "PLUMBING_TEST"))
  (shadow 'Servo (find-package "PLUMBING_TEST")))
(unless (find-package "PLUMBING_TEST::SERVO")
  (make-package "PLUMBING_TEST::SERVO"))

(in-package "ROS")
;;//! \htmlinclude Servo.msg.html


(defclass plumbing_test::Servo
  :super ros::object
  :slots (_servo_id _angle _speed ))

(defmethod plumbing_test::Servo
  (:init
   (&key
    ((:servo_id __servo_id) 0)
    ((:angle __angle) 0.0)
    ((:speed __speed) 0.0)
    )
   (send-super :init)
   (setq _servo_id (round __servo_id))
   (setq _angle (float __angle))
   (setq _speed (float __speed))
   self)
  (:servo_id
   (&optional __servo_id)
   (if __servo_id (setq _servo_id __servo_id)) _servo_id)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:serialization-length
   ()
   (+
    ;; int32 _servo_id
    4
    ;; float32 _angle
    4
    ;; float32 _speed
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _servo_id
       (write-long _servo_id s)
     ;; float32 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _servo_id
     (setq _servo_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _angle
     (setq _angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _speed
     (setq _speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get plumbing_test::Servo :md5sum-) "ec902b75210c8c8b2dfa408c2b1fa370")
(setf (get plumbing_test::Servo :datatype-) "plumbing_test/Servo")
(setf (get plumbing_test::Servo :definition-)
      "int32 servo_id

float32 angle

float32 speed

")



(provide :plumbing_test/Servo "ec902b75210c8c8b2dfa408c2b1fa370")


