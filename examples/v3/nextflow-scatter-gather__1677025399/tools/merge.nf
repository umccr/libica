process merge {
    container 'public.ecr.aws/lts/ubuntu:22.04'
    pod annotation: 'scheduler.illumina.com/presetSize', value: 'standard-small'
    cpus 1
    memory '512 MB'

    publishDir 'out', mode: 'symlink'

    input:
    path x

    output:
    path 'merged.tsv'

    """
    cat $x > merged.tsv
    """
}