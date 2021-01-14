import { classObject } from './cls'

export type clfObject = {
    text: string,
    value: string,
    specs?: Object<Array> // hier sowas wie type clfSpecsInterface = SvmSpecs | ...
}

interface ClfResponse {
    Z: number[]
}

interface TrainingSpecs {
    test_size: number
}

// intefaces für die Bereitstellung der Model-Optionen (NICHT die selectierten für das Modell, sondern für die Optionen)

interface SvmSpecs {
    kernel: string[]
}

interface RandomForestSpecs {
    lowerBoundEstimators: number,
    upperBoundEstimators: number
}

interface ModelSpecData {
    svmSpecs: SvmSpecs,
    randomForestSpecs: RandomForestSpecs
}

// type

export interface ClfState {
    classes: classObject[],
    currentClass: classObject,
    classifiers: clfObject[],
    selectedClassifier: clfObject | undefined,
    inputspace : Object,
    modelSpecData: ModelSpecData,
    clfResponse: ClfResponse,
    trainingSpecs: TrainingSpecs
}