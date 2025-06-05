nextflow.enable.dsl=2

include { sort } from 'tools/sort.nf'
include { split } from 'tools/split.nf'
include { merge } from 'tools/merge.nf'


params.myinput = "test.test"

workflow {
    input_ch = Channel.fromPath(params.myinput)
    split(input_ch)
    sort(split.out.flatten())
    merge(sort.out.collect())
}