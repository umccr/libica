process split {
    container 'public.ecr.aws/lts/ubuntu:22.04'
    pod annotation: 'scheduler.illumina.com/presetSize', value: 'standard-small'
    cpus 1
    memory '512 MB'

    input:
    path x

    output:
    path("split.*.tsv")

    """
    split -a10 -d -l3 --numeric-suffixes=1 --additional-suffix .tsv ${x} split.
    """
}