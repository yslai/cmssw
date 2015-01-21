#ifndef __UETable_h__
#define __UETable_h__

#include "CondFormats/Serialization/interface/Serializable.h"
#include <vector>

class UETable{
 public:
  UETable(){};
  std::vector<double> values;

  COND_SERIALIZABLE;
};

#endif
