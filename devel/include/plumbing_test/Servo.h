// Generated by gencpp from file plumbing_test/Servo.msg
// DO NOT EDIT!


#ifndef PLUMBING_TEST_MESSAGE_SERVO_H
#define PLUMBING_TEST_MESSAGE_SERVO_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace plumbing_test
{
template <class ContainerAllocator>
struct Servo_
{
  typedef Servo_<ContainerAllocator> Type;

  Servo_()
    : servo_id(0)
    , angle(0.0)
    , speed(0.0)  {
    }
  Servo_(const ContainerAllocator& _alloc)
    : servo_id(0)
    , angle(0.0)
    , speed(0.0)  {
  (void)_alloc;
    }



   typedef int32_t _servo_id_type;
  _servo_id_type servo_id;

   typedef float _angle_type;
  _angle_type angle;

   typedef float _speed_type;
  _speed_type speed;





  typedef boost::shared_ptr< ::plumbing_test::Servo_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::plumbing_test::Servo_<ContainerAllocator> const> ConstPtr;

}; // struct Servo_

typedef ::plumbing_test::Servo_<std::allocator<void> > Servo;

typedef boost::shared_ptr< ::plumbing_test::Servo > ServoPtr;
typedef boost::shared_ptr< ::plumbing_test::Servo const> ServoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::plumbing_test::Servo_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::plumbing_test::Servo_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::plumbing_test::Servo_<ContainerAllocator1> & lhs, const ::plumbing_test::Servo_<ContainerAllocator2> & rhs)
{
  return lhs.servo_id == rhs.servo_id &&
    lhs.angle == rhs.angle &&
    lhs.speed == rhs.speed;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::plumbing_test::Servo_<ContainerAllocator1> & lhs, const ::plumbing_test::Servo_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace plumbing_test

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::plumbing_test::Servo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::plumbing_test::Servo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::plumbing_test::Servo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::plumbing_test::Servo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::plumbing_test::Servo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::plumbing_test::Servo_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::plumbing_test::Servo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ec902b75210c8c8b2dfa408c2b1fa370";
  }

  static const char* value(const ::plumbing_test::Servo_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xec902b75210c8c8bULL;
  static const uint64_t static_value2 = 0x2dfa408c2b1fa370ULL;
};

template<class ContainerAllocator>
struct DataType< ::plumbing_test::Servo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "plumbing_test/Servo";
  }

  static const char* value(const ::plumbing_test::Servo_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::plumbing_test::Servo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 servo_id\n"
"\n"
"float32 angle\n"
"\n"
"float32 speed\n"
;
  }

  static const char* value(const ::plumbing_test::Servo_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::plumbing_test::Servo_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.servo_id);
      stream.next(m.angle);
      stream.next(m.speed);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Servo_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::plumbing_test::Servo_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::plumbing_test::Servo_<ContainerAllocator>& v)
  {
    s << indent << "servo_id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.servo_id);
    s << indent << "angle: ";
    Printer<float>::stream(s, indent + "  ", v.angle);
    s << indent << "speed: ";
    Printer<float>::stream(s, indent + "  ", v.speed);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PLUMBING_TEST_MESSAGE_SERVO_H