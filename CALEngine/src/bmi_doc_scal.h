#ifndef BMI_DOC_SCAL_H
#define BMI_DOC_SCAL_H
#include <unordered_set>
#include "bmi.h"
#include <string>
using namespace std; 
 class BMI_doc_scal:public BMI{
    int B = 1;
    int T, N;
    int R;
    std::map<int, int> docs_in_strata;
    public:
    BMI_doc_scal(Seed seed,
        Dataset *documents,
        int num_threads,
        int judgments_per_iteration,
        bool async_mode,
        int training_iterations,
        int scal_n);
    
    virtual void record_judgment_batch(std::vector<std::pair<std::string, int>> judgments);
    
    virtual void perform_iteration();
    
    virtual vector<int> perform_training_iteration();

    virtual string get_log() {
        string ret = "";
        for (map<int,int>::iterator it=docs_in_strata.begin();
            it!=docs_in_strata.end(); ++it){
            ret += documents->get_id(it->first) + " " + to_string(it->second)+"\n";
        }
        return ret;
    }
};
#endif // BMI_DOC_SCAL_H