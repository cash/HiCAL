#ifndef FEATURES_H
#define FEATURES_H

#include <string>
#include <vector>
#include <unordered_map>
#include "utils/features.h"
#include "sofiaml/sf-sparse-vector.h"
#include "dataset.h"

namespace features{

    void init(const std::string &fname);

    std::unordered_map<std::string, int> get_tf(const vector<std::string> &words);

    // Extract features from given text
    SfSparseVector get_features(const std::string &text, const Dataset &dataset, double max_norm=1);

}
#endif // FEATURES_H
