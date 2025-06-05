process sort {
    container 'public.ecr.aws/lts/ubuntu:22.04'
    pod annotation: 'scheduler.illumina.com/presetSize', value: 'standard-small'
    cpus 1
    memory '512 MB'

    input:
    path x

    output:
    path '*.sorted.tsv'

    """
    sort -gk1,1 $x > ${x.baseName}.sorted.tsv
    """
}